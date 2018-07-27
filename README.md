# LC-cli Patch

## Leetcode web session
Leetcode only allows for one web session per account. When a user (a unique IP) logs in, leetcode distributes a [csrftoken](https://github.com/pillarjs/understanding-csrf/blob/master/README_zh.md) and a LEETCODE_SESSION as liable keys for a validate web session. Only a user with a newest csrftoken & LEETCODE_SESSION will be recognized as a legit user, otherwise leetcode would require a re-login. So when multiple IP are visiting leetcode with the same account, only the last logged in IP (which has the latest csrftoken & LEETCODE_SESSION) can access leetcode, and all other IPs will be banned since their keys are obsolete.

The solution is to share csrftoken & LEETCODE_SESSION keys among multiple IPs. In other words, if multiple users (with different IPs) share the same configuration, they can share not only one leetcode account, but also the one leetcode web session, so leetcode web session limitation is not violated.  

[leetcode-cli](https://github.com/skygragon/leetcode-cli) (cli stands for command line interface) is a powerful command line tool for leetcode. By modifying its configuration a little bit we can access leetcode simultaneously. Documents for leetcode-cli is [here](https://skygragon.github.io/leetcode-cli/)

## Install 
### Install Leetcode-cli for Linux
```bash
bash install.sh
```

### Install Leetcode-cli for Windows/Mac
For other systems you need to install corresponding npm and nodejs. Then use:
```bash
npm install -g leetcode-cli
leetcode config autologin:enable false
```

## Usage
The key to sharing web session is to share newest configuration files (older configurations are invalidated by leetcode). **In this repo stores the latest configuration files in lc/.** This is done by keeping a server which always keeps and updates leetcode-cli configuration.

Each time before you use leetcode-cli, please synchronize your configuration with the server. Use this if you are linux:
```bash
bash ./loadconfig.sh
```
For other systems, you need to find your leetcode-cli `.lc/user.json` configuration directory, and cover it with `server:~/.lc/user.json` (see loadconfig.sh). 

Since sharers of leetcode account are using the same web session, their behaviors will also be synchronized. For example, when user A wants to submit code using leetcode-cli, user B happens to be changing session to his/her private session, A would be submitting code to B's session. So each time before you run / submit code, you need to `leetcode session -e YOUR_SESSION` to enable your session.

**Important: The server blocks all pretended log-ins, so you can't login yourself.**