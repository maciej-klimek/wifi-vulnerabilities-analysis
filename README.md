# Wi-Fi Vulnerabilities Analysis

> NOTE: This is a working repository for an engineering thesis. It was used to organize, set up, and document experiments. Consequently, the code and structure are functional for the research but may not be well-organized and fully complete.

This repository contains code, scripts, research results, and notes related to the engineering thesis titled *"Experimental Analysis of Modern Attacks Against IEEE 802.11 Networks"*. The thesis itself, available as `thesis.pdf`, offers a comprehensive report on this research, presenting a detailed analysis of the experiments, the results obtained, and the conclusions drawn from the study.

## Repository Structure

Some directories and subdirectories contain their own `README.md` files with more specific information about their usage and scripts they contain (e.g., `ssid-integrity-vulnerability/client-vulnerabilty-testing/README.md`).

Main directories of this repository:

*   `hostapd-scripts`: Helper scripts for building and configuring hostapd, used in some experiments.
*   `ssid-integrity-vulnerability` **(SIV)**: Contains code and scripts related to the study of the *SSID Confusion* vulnerability and associated attack scenarios.
    *   `client-vulnerability-testing`: Tools and testbeds client-side vulnerabilities evaluation. Based on the [ssid-confusion-hostap](https://github.com/vanhoefm/ssid-confusion-hostap) repository.
    *   `mc-mitm-experiments`: Scripts and setups for conducting multi-channel Man-in-the-Middle experiments. Based on the [mc-mitm](https://github.com/vanhoefm/mc-mitm) repository.
*   `queue-security-context` **(QSC)**: Contains code and scripts related to the study of frame queuing vulnerabilities in IEEE 802.11 networks (*Framing Frames*).
    *   `4wh-queue`: Scripts and implementation attempts for testing queuing mechanisms during the 4-way handshake.
    *   `macstealer`: Testbed and configurations for testing MAC address stealing scenarios. Based on the [macstealer](https://github.com/vanhoefm/macstealer) repository.
    *   `testcases`: A collection of Python testcases for the `wifi-framework`. Some test cases, such as SA Query test cases, are based on [wifi-framing](https://github.com/domienschepers/wifi-framing) repository.
    *   [`wifi-framework`](https://github.com/domienschepers/wifi-framework): Framework for orchestrating and automating Wi-Fi experiments.
*   `notes-captures-results`: A working folder containing notes, network traffic captures, test results, and other supporting materials used while writing the thesis.



## Engineering Thesis

The [thesis.pdf](thesis.pdf) file is the engineering thesis that serves as the main report and documentation of the conducted research. It describes the theoretical foundations of Wi-Fi networks, the analysis of the studied vulnerabilities, the course of the experiments, and the conclusions.

## Base Structure

```
├── hostapd-scripts
├── notes-captures-results
│   ├── macstealer
│   ├── misc
│   ├── queue-security-context
│   └── ssid-integrity-vulnerability
├── queue-security-context
│   ├── 4wh-queue
│   ├── macstealer-virtual
│   ├── testcases
│   └── wifi-framework
├── ssid-integrity-vulnerability
│   ├── client-vulnerabilty-testing
│   └── mc-mitm-experiments
└── thesis.pdf
```
