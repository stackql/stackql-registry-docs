---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - usertype
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.usertype.user" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="createdBy" /> | `string` |
| <CopyableCode code="default" /> | `boolean` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="lastUpdatedBy" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="typeId, subdomain" /> | Fetches a User Type by ID. The special identifier `default` may be used to fetch the default User Type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Fetches all User Types in your org |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Creates a new User Type. A default User Type is automatically created along with your org, and you may add another 9 User Types for a maximum of 10. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="typeId, subdomain" /> | Deletes a User Type permanently. This operation is not permitted for the default type, nor for any User Type that has existing users |
| <CopyableCode code="partialUpdate" /> | `EXEC` | <CopyableCode code="typeId, subdomain" /> | Updates an existing User Type |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="typeId, subdomain" /> | Replace an existing User Type |
