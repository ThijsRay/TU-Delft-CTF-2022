pragma solidity >=0.7.0 <0.9.0;


interface Contract{
    function getFlag() external view returns (uint);
}
contract Solve {

    address c;

    constructor () {
        c = 0x550986A6F7A03CA6E95825DB83074fEb3c1050c8;
    }

    function getFlag() external view returns (uint256) {
        return Contract(c).getFlag();
    }
}

