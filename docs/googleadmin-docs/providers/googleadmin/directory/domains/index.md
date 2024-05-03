---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creationTime" /> | `string` | Creation time of the domain. Expressed in [Unix time](https://en.wikipedia.org/wiki/Epoch_time) format. (Read-only). |
| <CopyableCode code="domainAliases" /> | `array` | A list of domain alias objects. (Read-only) |
| <CopyableCode code="domainName" /> | `string` | The domain name of the customer. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="isPrimary" /> | `boolean` | Indicates if the domain is a primary domain (Read-only). |
| <CopyableCode code="kind" /> | `string` | Kind of resource this is. |
| <CopyableCode code="verified" /> | `boolean` | Indicates the verification state of a domain. (Read-only). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customer, domainName" /> | Retrieves a domain of the customer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customer" /> | Lists the domains of the customer. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customer" /> | Inserts a domain of the customer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customer, domainName" /> | Deletes a domain of the customer. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customer" /> | Lists the domains of the customer. |
