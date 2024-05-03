---
title: domain_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_aliases
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.domain_aliases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | The creation time of the domain alias. (Read-only). |
| <CopyableCode code="domainAliasName" /> | `string` | The domain alias name. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="kind" /> | `string` | Kind of resource this is. |
| <CopyableCode code="parentDomainName" /> | `string` | The parent domain name that the domain alias is associated with. This can either be a primary or secondary domain name within a customer. |
| <CopyableCode code="verified" /> | `boolean` | Indicates the verification state of a domain alias. (Read-only) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customer, domainAliasName" /> | Retrieves a domain alias of the customer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customer, parentDomainName" /> | Lists the domain aliases of the customer. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customer" /> | Inserts a domain alias of the customer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customer, domainAliasName" /> | Deletes a domain Alias of the customer. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customer, parentDomainName" /> | Lists the domain aliases of the customer. |
