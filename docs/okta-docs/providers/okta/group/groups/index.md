---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - group
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.group.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="lastMembershipUpdated" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="objectClass" /> | `array` |
| <CopyableCode code="profile" /> | `object` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId, subdomain" /> | Fetches a group from your organization. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Enumerates groups in your organization with pagination. A subset of groups can be returned that match a supported filter expression or query. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Adds a new group with `OKTA_GROUP` type to your organization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, subdomain" /> | Removes a group with `OKTA_GROUP` type from your organization. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="groupId, subdomain" /> | Updates the profile for a group with `OKTA_GROUP` type from your organization. |
