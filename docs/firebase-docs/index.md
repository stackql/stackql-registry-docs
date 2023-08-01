---
title: firebase
hide_title: false
hide_table_of_contents: false
keywords:
  - firebase
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
id: firebase-doc
slug: /providers/firebase

---
Application development platform for creating mobile and web applications.  
    
:::info Provider Summary (v23.03.00121)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>9</b></span><br />
<span>total methods:&nbsp;<b>138</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>53</b></span><br />
<span>total selectable resources:&nbsp;<b>41</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `firebase` provider, run the following command:  

```bash
REGISTRY PULL firebase;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication


The following authentication methods are supported:
- `service_account`
- `interactive` for running interactive queries from Cloud Shell or other machines where the user is authenticated using `gcloud auth login`

> for more information on creating service accounts and key files, see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview).

### Service Account Environment Variable (default)

The following system environment variable is used by default:  

- `GOOGLE_CREDENTIALS` - contents of the `google` service account key json fileThis variable is sourced at runtime (from the local machine using export GOOGLE_CREDENTIALS=cat creds/my-sa-key.json` for example or as a CI variable/secret).

This variable is sourced at runtime (from the local machine using `export GOOGLE_CREDENTIALS=$(cat creds/my-sa-key.json)` for example or as a CI variable/secret).

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

### Interactive Authentication
When you are using Google Cloud Shell or on a machine where you have authenticated using `gcloud auth login`, you can then use the following authentication method:   

```bash
AUTH='{ "google": { "type": "interactive" }}'
stackql shell --auth="${AUTH}"
```

or using PowerShell:  

```powershell
$Auth = "{ 'google': { 'type': 'interactive' }}"
stackql.exe shell --auth=$Auth
```

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/firebase/firebase/">firebase</a><br />
<a href="/providers/firebase/firebaseappcheck/">firebaseappcheck</a><br />
<a href="/providers/firebase/firebasedatabase/">firebasedatabase</a><br />
<a href="/providers/firebase/firebasedynamiclinks/">firebasedynamiclinks</a><br />
<a href="/providers/firebase/firebasehosting/">firebasehosting</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/firebase/firebaseml/">firebaseml</a><br />
<a href="/providers/firebase/firebaserules/">firebaserules</a><br />
<a href="/providers/firebase/firebasestorage/">firebasestorage</a><br />
<a href="/providers/firebase/toolresults/">toolresults</a><br />
</div>
</div>