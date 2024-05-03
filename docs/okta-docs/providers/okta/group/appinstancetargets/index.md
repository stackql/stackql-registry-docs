---
title: appinstancetargets
hide_title: false
hide_table_of_contents: false
keywords:
  - appinstancetargets
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
<tr><td><b>Name</b></td><td><code>appinstancetargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.group.appinstancetargets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appName, applicationId, groupId, roleId, subdomain" /> | Add App Instance Target to App Administrator Role given to a Group |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, applicationId, groupId, roleId, subdomain" /> | Remove App Instance Target to App Administrator Role given to a Group |
