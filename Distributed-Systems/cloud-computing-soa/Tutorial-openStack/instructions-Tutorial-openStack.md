## Tutorial 2: Cloud Platform / OpenStack

This tutorial serves as a gentle introduction to cloud platforms as covered in the lecture. The primary goal is to learn how to use an Open Source Cloud Platform (**OpenStack**).

The main focus of this assignment is to teach you how to use the **OpenStack Web Interface (Horizon)** and the **OpenStack CLI** to manage the lifecycle of Virtual Machines (VMs).

> **Note:** In this tutorial, you will be given an account with limited privileges. It is not possible to perform advanced administrative tasks such as creating new projects, users, networks, or security groups.

---

### Objectives of this Assignment

* Get introductory hands-on experience with an Open Source Function as a Service platform (OpenStack).

### Learning Outcomes

1. Learn how to interact with a pre-installed OpenStack environment using Horizon and the CLI.

### Prerequisites

* Access to a pre-installed OpenStack instance.

---

## Table of Contents

1. [Step 1: OpenStack Web Interface (Horizon)](#step-1-openstack-web-interface-horizon)
2. [Step 2: OpenStack Command Line Interface (CLI)](#step-2-openstack-command-line-interface-cli)
3. [Submission & Grading](#submission-grading)

---

## Step 1: OpenStack Web Interface (Horizon)

### 1. Login to OpenStack Web Interface

* **URL:** <https://xd1.lab.uvalight.net/horizon/>
* Login with your provided credentials.

!\[Alt text\](images/login-OpenStack.png)

* Upon logging in, you will see a summary page. The menu on the left will adjust based on your account roles.

!\[image representing the overview/ dashboard UI of the Users resource in OpenStak \](images/overview-OpenStack.png)

### 2. Create a Project (Not covered)

You will see only one project named `groupXX` already created for you.

!\[image representing the project UI of OpenStack\](images/projects-OpenStack.png)

### 3. Create a User (Not covered)

Administrative users can create users via **Identity > Users**.

!\[image representing the Users management UI of OpenStack\](images/users-OpenStack.png)

* *Resource:* [Video: Create OpenStack User (15:42)](https://www.freecodecamp.org/)

### 4. Create a Network/Router (Not covered)

Administrative users can create networks via **Identity > Networks**.

* *Resource:* [Video: Create Private Network and Router (21:54)](https://www.freecodecamp.org/)

### 5. Create an Image (Not covered)

View existing images via **Project > Compute > Images**. You can use existing images or upload a virtual image file using the "Create Image" menu.

!\[image representing the VM management UI of OpenStack\](images/images-OpenStack.png)

* *Resource:* [Video: Manage and Creating Images (17:56)](https://www.freecodecamp.org/)

### 6. Security / Modify Group (TODO)

To SSH into your VM from a remote client, you must modify the security group to allow SSH traffic.

* *Resource:* [Video: Create a Security Group (26:17)](https://www.freecodecamp.org/)

### 7. Create/Start an Image Instance (TODO)

Launch an instance of the image and SSH into it from a remote machine.

* *Resource:* [Video: Create Instance (31:26)](https://www.freecodecamp.org/)

---

## Step 2: OpenStack Command Line Interface (CLI)

### 1. Installing OpenStack Client (TODO)

Before installing the client, create configuration files to handle authentication.

#### Configuration Files

Create the directory:

```bash
$ mkdir -p ~/.config/openstack
```

**Example:** `~/.config/openstack/clouds.yaml`

YAML

```
clouds:
  openstack:
    auth:
      auth_url: [https://xd1.lab.uvalight.net/keystone/v3/](https://xd1.lab.uvalight.net/keystone/v3/)
      username: "your-username"
      project_id: <your-project-ID>
      project_name: "your-project-name"
      user_domain_name: "Default"
    region_name: "RegionOne"
    interface: "public"
    identity_api_version: 3
```

**Example:** `openstackrc` **(Environment Variables)**

Bash

```
export OS_USERNAME="username"
export OS_PASSWORD="passwd"
export OS_PROJECT_NAME="project-name"
export OS_USER_DOMAIN_NAME="Default"
export OS_PROJECT_DOMAIN_NAME="Default"
export OS_AUTH_URL="[https://xd1.lab.uvalight.net/keystone/v3/](https://xd1.lab.uvalight.net/keystone/v3/)"
export OS_IDENTITY_API_VERSION=3
export OS_REGION_NAME="RegionOne"
```

#### Installation

Bash

```
# Update pip (Optional)
$ pip install pip --upgrade

# Install the client
$ pip install python-openstackclient
```

#### Authentication

If you are not using an `openrc` file, you must provide credentials manually:

Bash

```
$ openstack --os-username YOUR_USERNAME \
            --os-password YOUR_PASSWORD \
            --os-project-name YOUR_PROJECT_NAME \
            --os-region-name YOUR_REGION_NAME \
            --os-user-domain-name YOUR_USER_DOMAIN_NAME \
            --os-project-domain-name YOUR_PROJECT_DOMAIN_NAME \
            COMMAND
```

### OpenStack Commands (TODO)

There are two ways to use the CLI:

**Interactive Shell:**

Bash

```
$ openstack
(openstack) server list
```

**Direct Commands:**

Bash

```
$ openstack server list
$ openstack --os-cloud openstack server list
```

**Help Commands:**

Bash

```
$ openstack help
$ openstack help <command>
```