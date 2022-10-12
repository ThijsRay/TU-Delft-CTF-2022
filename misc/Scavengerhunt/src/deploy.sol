pragma solidity >=0.7.0 <0.9.0;

contract Flag{

    uint256 flag;

    constructor() {
        flag = 34692613931332538918678374955902730717960752524158095361649680765;
    }
    function getFlag() public view returns (uint256){
        return flag;
    }
}

