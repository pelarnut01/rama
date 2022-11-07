# Migrate Rama Monitor Project

This template demonstrates how to backup grafana and influxdb to new server

# 2.Setup

**Requirements**

1. node version 12.22.9 or later
2. influxdb version 2.5
3. grafana version 9.2.2
4. Ubuntu 18.04 or later

# 3.Installation

This section can be skipped if all requiremetns from **section 1:Septup** have been met.

### 3.1. Node.js (v12.22.9 or later)

1. It is recommended to install using `nvm` [(Node Version Manager)](https://github.com/nvm-sh/nvm)

   **_Command_**

   ```none
   wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
   ```

2. After `nvm` has been installed, append the following command to the end of `.profile`

   ```none
   sudo nano ~/.profile
   ```

   ```bash
   export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
   ```

3. Exit and save the `.profile` file

   Exit the file

   ```none
   CTRL+X
   ```

   Enter `Y` to save the file and press `ENTER` to confirm

   ```none
   Y
   ```

4. Restart `.profile`

   ```none
   . ~/.profile
   ```

5. Check if `nvm` has been successfully installed

   ```none
   nvm --version
   ```

   **_Example Output_**

   ```none
   0.39.1
   ```

6. Install Node.js v12.22.9

   ```none
   nvm install 12.22.9
   ```

7. Set Node.js v12.22.9 as default

   ```none
   nvm alias default 12.22.9
   ```

8. Check Node.js version and make sure it is v12.22.9

   ```none
   node --version
   ```

   **_Example Output_**

   ```none
   v12.22.9
   ```

### 3.2. Install Grafana

1. Install the latest OSS release:

   ```
   sudo apt-get install -y apt-transport-https
   sudo apt-get install -y software-properties-common wget
   sudo wget -q -O /usr/share/keyrings/grafana.key https://packages.grafana.com/gpg.key
   ```

2. Add this repository for stable releases:

   ```
   echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
   ```

3. After you add the repository:
   ```
   sudo apt-get update
   sudo apt-get install grafana
   ```
4. Start the server with systemd

   ```
   sudo systemctl daemon-reload
   sudo systemctl start grafana-server
   sudo systemctl status grafana-server
   ```

   4.1 Configure the Grafana server to start at boot:

   ```
   sudo systemctl enable grafana-server.service
   ```

### 3.3. Install Influxdb

1.  InfluxDB 2.x Open Source Time Series Database

    ```
    $ wget -q https://repos.influxdata.com/influxdb.key
    ```

    ```
    $ echo '23a1c8836f0afc5ed24e0486339d7cc8f6790b83886c4c96995b88a061c5bb5d influxdb.key' | sha256sum -c && cat influxdb.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdb.gpg > /dev/null
    ```

    ```
    $ echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdb.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
    ```

    ```
    $ sudo apt-get update && sudo apt-get install influxdb2
    ```

2.  Install InfluxDB as a service with systemd

    ```
    $ wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.5.0-xxx.deb
    $ sudo dpkg -i influxdb2-2.5.0-arm64.deb
    ```

3.  Start the InfluxDB service

    ```
    sudo service influxdb start
    ```

    3.1 Restart your system and verify that the service is running correctly

    ```
    $ sudo service influxdb status

    ● influxdb.service - InfluxDB is an open-source, distributed, time series database
    Loaded: loaded (/lib/systemd/system/influxdb.service; enabled; vendor preset: enable>
    Active: active (running)
    ```

# 4.Back up and restore Influxdb

An easy, step-by-step guide to migrate InfluxDB data from legacy (1.x) to new version (2.x)

1.  Backup Influxdb
    For details, please see https://github.com/dvsu/influxdb-migration.git , After backup from the old influxdb . you get the folder stored data line protocol.
2.  Restore Influxdb
    Please clone project https://github.com/pelarnut01/rama.git

    2.1 Configuration in file restore.js

    - **Url** Enter the influxdb IP address and append it with **/api/v2/write**.
    - **Organization** Enter organization name can setting on influxdb.
    - **Bucket** Enter Bucket name can setting on influxdb.
    - **Data_path** Enter path to folder stored data line protocol

    **Run command**

        Going to the parent directory of a file restore.js

        $ node restore.js

# 5.Setup MQTT Subscribe

Restore
git@github.com:pelarnut01/Nodered-rama.git

setup auto run
open command

```
crontab -e
enter 1
```

add code in last line

```
@reboot sleep 20; node /home/influxdb/Desktop/mqtt/mqttget.js
```

Save and Exit

Reboot system
command

```
@reboot
```
