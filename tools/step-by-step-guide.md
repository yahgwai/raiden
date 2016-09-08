# Nodes

## blockchain

- runs `geth`
- opens rpc

IP: 192.168.0.73

## consumer
- rpi
- runs `raiden`
- connects to blockchain via rpc

IP: 192.168.0.101

## supplier
- rpi
- runs `raiden`
- connects to blockchain via rpc

IP: 192.168.0.102

# Commands

    export CONFIG_DIR="/tmp/iot-config"
    export GETH="192.168.0.73"
    export GETH_DATADIR="/tmp/iot-demo"
    export RAIDEN_NODES="192.168.0.101 192.168.0.102"
    rm -rf $CONFIG_DIR
    mkdir -p $CONFIG_DIR/geth/keystore

    ./tools/config_builder.py geth_commands $GETH_DATADIR $GETH > $CONFIG_DIR/geth_command.json

    ./tools/config_builder.py accounts 1 $RAIDEN_NODES > $CONFIG_DIR/raiden_accounts.json

    ./tools/config_builder.py build_scenario 1 $RAIDEN_NODES > $CONFIG_DIR/scenario.json

    ./tools/config_builder.py full_genesis 1 $RAIDEN_NODES --scenario $CONFIG_DIR/scenario.json > $CONFIG_DIR/genesis.json

    ./tools/config_builder.py account_file > $CONFIG_DIR/geth/keystore/account.json

Now $CONFIG_DIR contains several files:

- `scenario.json`: interesting bit for demo is `assets[0].token_address`
- `raiden_accounts.json`: privatekeys to use for the two nodes on both machines

- `geth`-directory: move this to your geth node to the folder $GETH_DATADIR
- `geth/geth_commands.json` contains the command to start the geth node. After you run this, both raiden nodes can
  communicate with the network using:

    --rpc_endpoint "192.168.0.73:8545"

and the other `raiden_flags` from $CONFIG_DIR/genesis.json:config['raidenFlags']
