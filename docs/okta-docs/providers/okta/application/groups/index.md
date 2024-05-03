---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - application
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
<tr><td><b>Id</b></td><td><CopyableCode code="okta.application.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="priority" /> | `integer` |
| <CopyableCode code="profile" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appId, groupId, subdomain" /> | Fetches an application group assignment |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appId, subdomain" /> | Enumerates group assignments for an application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appId, groupId, subdomain" /> | Removes a group assignment from an application. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appId, groupId, subdomain" /> | Assigns a group to an application |
