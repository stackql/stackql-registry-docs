---
title: okta
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - identity
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
id: okta-doc
slug: /providers/okta

---
Authentication and authorization services.  
    
:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>24</b></span><br />
<span>total methods:&nbsp;<b>283</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>73</b></span><br />
<span>total selectable resources:&nbsp;<b>66</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `okta` provider, run the following command:  

```bash
REGISTRY PULL okta;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  


## Authentication

The `OKTA_API_TOKEN` environment variable is used by default to store credentials to authorize requests to Okta.  This variable is sourced at runtime (from the local machine or as a CI variable/secret).  More information on obtaining a Okta API Token can be found [here](https://developer.okta.com/docs/guides/create-an-api-token/).  

<details>

<summary>Using a different environment variable</summary>

To use a different environment variable (instead of the default), use the `--auth` flag of the `stackql` program.  For example:  

```bash
AUTH='{ "okta": { "type": "api_key",  "credentialsenvvar": "YOUR_OKTA_API_TOKEN_VAR", "valuePrefix": "SSWS " }}'
stackql shell --auth="${AUTH}"
```
or using PowerShell:  

```powershell
$Auth = "{ 'okta': { 'type': 'api_key',  'credentialsenvvar': 'YOUR_OKTA_API_TOKEN_VAR', 'valuePrefix': 'SSWS ' }}"
stackql.exe shell --auth=$Auth
```

</details>

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/okta/application/">application</a><br />
<a href="/providers/okta/authenticator/">authenticator</a><br />
<a href="/providers/okta/authorizationserver/">authorizationserver</a><br />
<a href="/providers/okta/domain/">domain</a><br />
<a href="/providers/okta/eventhook/">eventhook</a><br />
<a href="/providers/okta/feature/">feature</a><br />
<a href="/providers/okta/group/">group</a><br />
<a href="/providers/okta/groupschema/">groupschema</a><br />
<a href="/providers/okta/identityprovider/">identityprovider</a><br />
<a href="/providers/okta/inlinehook/">inlinehook</a><br />
<a href="/providers/okta/linkedobject/">linkedobject</a><br />
<a href="/providers/okta/log/">log</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/okta/networkzone/">networkzone</a><br />
<a href="/providers/okta/org/">org</a><br />
<a href="/providers/okta/policy/">policy</a><br />
<a href="/providers/okta/profilemapping/">profilemapping</a><br />
<a href="/providers/okta/session/">session</a><br />
<a href="/providers/okta/template/">template</a><br />
<a href="/providers/okta/threatinsight/">threatinsight</a><br />
<a href="/providers/okta/trustedorigin/">trustedorigin</a><br />
<a href="/providers/okta/user/">user</a><br />
<a href="/providers/okta/userfactor/">userfactor</a><br />
<a href="/providers/okta/userschema/">userschema</a><br />
<a href="/providers/okta/usertype/">usertype</a><br />
</div>
</div>
