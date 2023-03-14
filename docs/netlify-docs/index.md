---
title: netlify
hide_title: false
hide_table_of_contents: false
keywords:
  - netlify
  - cdn
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
id: netlify-doc
slug: /providers/netlify

---
Web development and content distribution platform.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>30</b></span><br />
<span>total methods:&nbsp;<b>105</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>51</b></span><br />
<span>total selectable resources:&nbsp;<b>31</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `netlify` provider, run the following command:  

```bash
REGISTRY PULL netlify;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  


## Authentication

The `NETLIFY_TOKEN` environment variable is used by default to store credentials to authorize requests to Netlify.  This variable is sourced at runtime (from the local machine or as a CI variable/secret).  More information on obtaining a Netlify API Token can be found [here](https://docs.netlify.com/api/get-started/#authentication).  

<details>

<summary>Using a different environment variable</summary>

To use a different environment variable (instead of the default), use the `--auth` flag of the `stackql` program.  For example:  

```bash
AUTH='{ "netlify": { "type": "bearer",  "credentialsenvvar": "YOUR_NETLIFY_TOKEN_VAR" }}'
stackql shell --auth="${AUTH}"
```
or using PowerShell:  

```powershell
$Auth = "{ 'netlify': { 'type': 'bearer',  'credentialsenvvar': 'YOUR_NETLIFY_TOKEN_VAR' }}"
stackql.exe shell --auth=$Auth
```

</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/netlify/access_token/">access_token</a><br />
<a href="/providers/netlify/account_membership/">account_membership</a><br />
<a href="/providers/netlify/account_type/">account_type</a><br />
<a href="/providers/netlify/asset/">asset</a><br />
<a href="/providers/netlify/asset_public_signature/">asset_public_signature</a><br />
<a href="/providers/netlify/audit_log/">audit_log</a><br />
<a href="/providers/netlify/build/">build</a><br />
<a href="/providers/netlify/build_hook/">build_hook</a><br />
<a href="/providers/netlify/build_log_msg/">build_log_msg</a><br />
<a href="/providers/netlify/deploy/">deploy</a><br />
<a href="/providers/netlify/deploy_key/">deploy_key</a><br />
<a href="/providers/netlify/deployed_branch/">deployed_branch</a><br />
<a href="/providers/netlify/dns_zone/">dns_zone</a><br />
<a href="/providers/netlify/file/">file</a><br />
<a href="/providers/netlify/form/">form</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/netlify/function/">function</a><br />
<a href="/providers/netlify/hook/">hook</a><br />
<a href="/providers/netlify/hook_type/">hook_type</a><br />
<a href="/providers/netlify/member/">member</a><br />
<a href="/providers/netlify/metadata/">metadata</a><br />
<a href="/providers/netlify/payment_method/">payment_method</a><br />
<a href="/providers/netlify/service/">service</a><br />
<a href="/providers/netlify/service_instance/">service_instance</a><br />
<a href="/providers/netlify/site/">site</a><br />
<a href="/providers/netlify/sni_certificate/">sni_certificate</a><br />
<a href="/providers/netlify/snippet/">snippet</a><br />
<a href="/providers/netlify/split_test/">split_test</a><br />
<a href="/providers/netlify/submission/">submission</a><br />
<a href="/providers/netlify/ticket/">ticket</a><br />
<a href="/providers/netlify/user/">user</a><br />
</div>
</div>
