---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - integrations
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the integration. |
| <CopyableCode code="description" /> | `string` | Optional. |
| <CopyableCode code="active" /> | `boolean` | Required. If any integration version is published. |
| <CopyableCode code="createTime" /> | `string` | Required. Output only. Auto-generated. |
| <CopyableCode code="creatorEmail" /> | `string` | Output only. The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| <CopyableCode code="lastModifierEmail" /> | `string` | Required. The last modifier of this integration |
| <CopyableCode code="updateTime" /> | `string` | Output only. Auto-generated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_integrations_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of all integrations in the specified project. |
| <CopyableCode code="projects_locations_products_integrations_list" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Returns the list of all integrations in the specified project. |
| <CopyableCode code="projects_locations_integrations_delete" /> | `DELETE` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Delete the selected integration and all versions inside |
| <CopyableCode code="projects_locations_integrations_execute" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Executes integrations synchronously by passing the trigger id in the request body. The request is not returned until the requested executions are either fulfilled or experienced an error. If the integration name is not specified (passing `-`), all of the associated integration under the given trigger_id will be executed. Otherwise only the specified integration for the given `trigger_id` is executed. This is helpful for execution the integration from UI. |
| <CopyableCode code="projects_locations_integrations_schedule" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Schedules an integration for execution by passing the trigger id and the scheduled time in the request body. |
| <CopyableCode code="projects_locations_integrations_test" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, projectsId" /> | Execute the integration in draft state |
| <CopyableCode code="projects_locations_products_integrations_execute" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, productsId, projectsId" /> | Executes integrations synchronously by passing the trigger id in the request body. The request is not returned until the requested executions are either fulfilled or experienced an error. If the integration name is not specified (passing `-`), all of the associated integration under the given trigger_id will be executed. Otherwise only the specified integration for the given `trigger_id` is executed. This is helpful for execution the integration from UI. |
| <CopyableCode code="projects_locations_products_integrations_schedule" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, productsId, projectsId" /> | Schedules an integration for execution by passing the trigger id and the scheduled time in the request body. |
| <CopyableCode code="projects_locations_products_integrations_test" /> | `EXEC` | <CopyableCode code="integrationsId, locationsId, productsId, projectsId" /> | Execute the integration in draft state |

## `SELECT` examples

Returns the list of all integrations in the specified project.

```sql
SELECT
name,
description,
active,
createTime,
creatorEmail,
lastModifierEmail,
updateTime
FROM google.integrations.integrations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>integrations</code> resource.

```sql
/*+ delete */
DELETE FROM google.integrations.integrations
WHERE integrationsId = '{{ integrationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
