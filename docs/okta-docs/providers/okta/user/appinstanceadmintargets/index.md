---
title: appinstanceadmintargets
hide_title: false
hide_table_of_contents: false
keywords:
  - appinstanceadmintargets
  - user
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
<tr><td><b>Name</b></td><td><code>appinstanceadmintargets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.user.appinstanceadmintargets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appName, applicationId, roleId, userId, subdomain" /> | Add App Instance Target to App Administrator Role given to a User |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, applicationId, roleId, userId, subdomain" /> | Remove App Instance Target to App Administrator Role given to a User |
