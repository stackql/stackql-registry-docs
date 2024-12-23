---
title: databricks_account
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
id: databricks_account-doc
slug: /providers/databricks_account
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Account-level features, identity and provisioning for Databricks.

:::info

For Databricks workspace operations use the [__`databricks_workspace`__](https://databricks-workspace.stackql.io/providers/databricks_workspace/) provider.

:::


:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>7</b></span><br />
<span>total resources:&nbsp;<b>31</b></span><br />
<span>total methods:&nbsp;<b>111</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL databricks_account;
```

## Authentication

To use the databricks_account, set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.  

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/databricks_account/billing/">billing</a><br />
<a href="/providers/databricks_account/iam/">iam</a><br />
<a href="/providers/databricks_account/logging/">logging</a><br />
<a href="/providers/databricks_account/oauth/">oauth</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/databricks_account/provisioning/">provisioning</a><br />
<a href="/providers/databricks_account/settings/">settings</a><br />
<a href="/providers/databricks_account/unity_catalog/">unity_catalog</a><br />
</div>
</div>