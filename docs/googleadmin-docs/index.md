---
title: googleadmin
hide_title: false
hide_table_of_contents: false
keywords:
  - googleadmin
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
id: googleadmin-doc
slug: /providers/googleadmin
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Google Workspace identity services.  
    
:::info Provider Summary (v23.07.00153)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>1</b></span><br />
<span>total methods:&nbsp;<b>139</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>28</b></span><br />
<span>total selectable resources:&nbsp;<b>25</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `googleadmin` provider, run the following command:  

```bash
REGISTRY PULL googleadmin;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication


The following authentication methods are supported:
- <CopyableCode code="service_account" /> (using a Google Cloud service account)

> for more information on creating service accounts and key files, see .

### Setup instructions

To authorize a Google Cloud service account for use in the Admin SDK, follow the instructions provided here:  

<details>

<summary>1. Create a Service Account (from the Google Cloud Console)</summary>

- Create a Google Cloud service account (see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview)).
- Download the JSON key file for the service account (see [Service account keys](https://cloud.google.com/iam/docs/service-account-creds#key-types)).
- From the Google Cloud Console, locate and select the service account created, go to __"Details" > "Advanced settings" > "Domain-wide delegation"__. 
- Copy the __"Client ID"__ of the service account to the clipboard.
- Click the __"VIEW GOOGLE WORKSPACE ADMIN CONSOLE"__ link. This will open the Google Workspace Admin Console in a new tab.

</details>

<details>

<summary>2. Enable the Admin SDK API for your project (from the Google Cloud Console)</summary>

- From the Google Cloud Console, in the same project that you created the Service Account in step 1, go to __"APIs & Services" > "Library"__.
- Search for __"Admin SDK API"__ and click on it.
- Click __"Enable"__.

</details>

<details>

<summary>3. Delegate Domain-Wide Authority to your Service Account (from the Google Workspace Admin Console)</summary>

- From the Google Workspace Admin Console, go to __"Security" > "Access and data control" > "API Controls" > "Domain-wide delegation" > "MANAGE DOMAIN-WIDE DELEGATION"__.
- Click __"Add new"__ and paste the __"Client ID"__ of the service account copied to the clipboard in step 1.
- In the __"OAuth scopes"__ field, enter the following scopes: __`https://www.googleapis.com/auth/cloud-platform`__ and __`https://www.googleapis.com/auth/admin.directory.user.readonly`__.
- Click __"Authorise"__.

</details>

<details>

<summary>4. Assign the Admin role to your Service Account (from the Google Workspace Admin Console)</summary>

- From the Google Workspace Admin Console, go to __"Account" > "Admin roles" > "User Management" > "Admins" > "Assign service accounts"__.
- Add the email to the service account created in step 1 and click __"Assign Role"__.  For more information, see [Assigning a role to a service account](https://developers.google.com/workspace/guides/create-credentials#assign_a_role_to_a_service_account).

</details>

### Service Account Environment Variable (default)

The following system environment variable is used by default:  

- <CopyableCode code="GOOGLE_CREDENTIALS" /> - contents of the <code>google</code> service account key json file

This variable is sourced at runtime (from the local machine using `export GOOGLE_CREDENTIALS=cat creds/my-sa-key.json` for example or as a CI variable/secret).

<details>

<summary>Specifying the service account key file location directly</summary>

You can specify the path to the service account key file without using the default environment variable by using the `--auth` flag of the `stackql` program.  For example:  

```bash
AUTH='{ "google": { "type": "service_account",  "credentialsfilepath": "creds/sa-key.json" }}'
stackql shell --auth="${AUTH}"
```

or using PowerShell:  

```powershell
$Auth = "{ 'google': { 'type': 'service_account',  'credentialsfilepath': 'creds/sa-key.json' }}"
stackql.exe shell --auth=$Auth
```

</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/googleadmin/directory/">directory</a><br />
</div>
<div class="providerDocColumn">
</div>
</div>
