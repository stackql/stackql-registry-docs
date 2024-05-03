---
title: apptargets
hide_title: false
hide_table_of_contents: false
keywords:
  - apptargets
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
<tr><td><b>Name</b></td><td><code>apptargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.group.apptargets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="category" /> | `string` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="features" /> | `array` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="signOnModes" /> | `array` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="verificationStatus" /> | `string` |
| <CopyableCode code="website" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupId, roleId, subdomain" /> | Lists all App targets for an `APP_ADMIN` Role assigned to a Group. This methods return list may include full Applications or Instances. The response for an instance will have an `ID` value, while Application will not have an ID. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appName, groupId, roleId, subdomain" /> | Success |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, groupId, roleId, subdomain" /> | Success |
