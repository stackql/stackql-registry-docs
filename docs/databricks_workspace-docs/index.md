---
title: databricks_workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - databricks
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
id: databricks_workspace-doc
slug: /providers/databricks_workspace
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Manage clusters, jobs, notebooks, MLflow and other Databricks workspace resources.

:::info

For Databricks account operations use the [__`databricks_account`__](https://databricks-account.stackql.io/providers/databricks_account/) provider.

:::


:::info Provider Summary

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>18</b></span><br />
<span>total resources:&nbsp;<b>186</b></span><br />
<span>total methods:&nbsp;<b>579</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL databricks_workspace;
```

## Authentication

To use the databricks_workspace, set the following environment variables:

- <CopyableCode code="DATABRICKS_ACCOUNT_ID" /> - a uuid representing your Databricks account id, you can get this from the Databricks UI (see <a href="https://docs.databricks.com/en/admin/account-settings/index.html#locate-your-account-id">Locate your account id</a>)
- <CopyableCode code="DATABRICKS_CLIENT_ID" /> - obtained after creating a service principal through the Databricks UI (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)
- <CopyableCode code="DATABRICKS_CLIENT_SECRET" /> - obtained after creating a service principal secret through the Databricks UI, using the "Generate Secret" function (see <a href="https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html">Authenticate access to Databricks with a service principal using OAuth</a>)

These are the same variables that Terraform, the Databricks SDKs, and CLI use.  

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/databricks_workspace/apps/">apps</a><br />
<a href="/providers/databricks_workspace/cleanrooms/">cleanrooms</a><br />
<a href="/providers/databricks_workspace/compute/">compute</a><br />
<a href="/providers/databricks_workspace/dbsql/">dbsql</a><br />
<a href="/providers/databricks_workspace/deltalivetables/">deltalivetables</a><br />
<a href="/providers/databricks_workspace/deltasharing/">deltasharing</a><br />
<a href="/providers/databricks_workspace/filemanagement/">filemanagement</a><br />
<a href="/providers/databricks_workspace/iam/">iam</a><br />
<a href="/providers/databricks_workspace/lakeview/">lakeview</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/databricks_workspace/machinelearning/">machinelearning</a><br />
<a href="/providers/databricks_workspace/marketplace/">marketplace</a><br />
<a href="/providers/databricks_workspace/realtimeserving/">realtimeserving</a><br />
<a href="/providers/databricks_workspace/repos/">repos</a><br />
<a href="/providers/databricks_workspace/secrets/">secrets</a><br />
<a href="/providers/databricks_workspace/unitycatalog/">unitycatalog</a><br />
<a href="/providers/databricks_workspace/vectorsearch/">vectorsearch</a><br />
<a href="/providers/databricks_workspace/workflows/">workflows</a><br />
<a href="/providers/databricks_workspace/workspace/">workspace</a><br />
</div>
</div>