---
title: default
hide_title: false
hide_table_of_contents: false
keywords:
  - default
  - userschema
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
<tr><td><b>Name</b></td><td><code>default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.userschema.default" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="$schema" /> | `string` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="definitions" /> | `object` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="properties" /> | `object` |
| <CopyableCode code="title" /> | `string` |
| <CopyableCode code="type" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appInstanceId, subdomain" /> | Fetches the Schema for an App User |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="appInstanceId, subdomain" /> | Partial updates on the User Profile properties of the Application User Schema. |
