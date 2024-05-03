---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - rum
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.rum.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | RUM application ID. |
| <CopyableCode code="attributes" /> | `object` | RUM application attributes. |
| <CopyableCode code="type" /> | `string` | RUM application response type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_rum_application" /> | `SELECT` | <CopyableCode code="id, dd_site" /> | Get the RUM application with given ID in your organization. |
| <CopyableCode code="get_rum_applications" /> | `SELECT` | <CopyableCode code="dd_site" /> | List all the RUM applications in your organization. |
| <CopyableCode code="create_rum_application" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a new RUM application in your organization. |
| <CopyableCode code="delete_rum_application" /> | `DELETE` | <CopyableCode code="id, dd_site" /> | Delete an existing RUM application in your organization. |
| <CopyableCode code="_get_rum_application" /> | `EXEC` | <CopyableCode code="id, dd_site" /> | Get the RUM application with given ID in your organization. |
| <CopyableCode code="_get_rum_applications" /> | `EXEC` | <CopyableCode code="dd_site" /> | List all the RUM applications in your organization. |
| <CopyableCode code="update_rum_application" /> | `EXEC` | <CopyableCode code="id, data__data, dd_site" /> | Update the RUM application with given ID in your organization. |
