pragma solidity >=0.8.0 <0.9.0;

// SPDX-License-Identifier: GPL-3.0

contract Game {

    address private _owner;

    mapping (address => Player) addressToPlayer;

    struct Player{
        bool land;
        uint gold;
        uint collectors;
        uint multiplier;
        uint lastCheck;
    }

    modifier onlyOwner() {
        require(msg.sender == _owner, "Ownable: caller is not the owner");
        _;
    }

    modifier ownsLand() {
        require(addressToPlayer[msg.sender].land == true, "you do not have a land");
        _;
    }

    constructor() {
        _owner = msg.sender;
    }

    function buyLand() external payable {
        require(msg.value == 1 ether, "not sending 1 ether");
        require(addressToPlayer[msg.sender].land == false, "you already have a land");
        addressToPlayer[msg.sender] = Player(true, 100, 0, 0, block.timestamp);
    }

    function buyCollector() external ownsLand {
        refresh();
        require(addressToPlayer[msg.sender].gold >= 30, "not enough gold");
        addressToPlayer[msg.sender].gold -= 30;
        addressToPlayer[msg.sender].collectors += 1;
        if (addressToPlayer[msg.sender].multiplier == 0) {
            addressToPlayer[msg.sender].multiplier = 1;
        }
        refresh();
    }

    function upgradeMultiplier() public ownsLand {
        refresh();
        require(addressToPlayer[msg.sender].gold >= 300, "not enough gold");
        addressToPlayer[msg.sender].gold -= 300;
        addressToPlayer[msg.sender].multiplier *= 2;
        refresh();

    }

    function refresh() public {
        addressToPlayer[msg.sender].gold += ((uint(block.timestamp) - uint(addressToPlayer[msg.sender].lastCheck)) * addressToPlayer[msg.sender].collectors ) * addressToPlayer[msg.sender].multiplier;
        addressToPlayer[msg.sender].lastCheck = uint(block.timestamp);
        winGame();
    }

    function display() public returns (uint[] memory){
        uint[] memory response = new uint[](3);
        response[0] = addressToPlayer[msg.sender].gold;
        response[1] = addressToPlayer[msg.sender].collectors;
        response[2] = addressToPlayer[msg.sender].multiplier;
        return response;
    }

    function winGame() public ownsLand {
        if (addressToPlayer[msg.sender].gold >= uint(100000)){
            if(addressToPlayer[msg.sender].collectors >= uint(10)){
                addressToPlayer[msg.sender].land = false;
                addressToPlayer[msg.sender].gold = 0;
                addressToPlayer[msg.sender].collectors = 0;
                addressToPlayer[msg.sender].multiplier = 0;
                addressToPlayer[msg.sender].lastCheck = 0;
                payable(msg.sender).transfer(address(this).balance);
            }
        }
    }

    function money() public view returns(uint){
        return address(this).balance;
    }
    function withdraw() external onlyOwner payable {
        payable(_owner).transfer(address(this).balance);
    }
}
