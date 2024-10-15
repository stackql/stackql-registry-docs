---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the API. The name of the operation being performed on this particular object. It should match the action name that appears in RBAC / the event service. Examples of operations include: * Microsoft.Compute/virtualMachine/capture/action * Microsoft.Compute/virtualMachine/restart/action * Microsoft.Compute/virtualMachine/write * Microsoft.Compute/virtualMachine/read * Microsoft.Compute/virtualMachine/delete Each action should include, in order: (1) Resource Provider Namespace (2) Type hierarchy for which the action applies (e.g. server/databases for a SQL Azure database) (3) Read, Write, Action or Delete indicating which type applies. If it is a PUT/PATCH on a collection or named value, Write should be used. If it is a GET, Read should be used. If it is a DELETE, Delete should be used. If it is a POST, Action should be used. As a note: all resource providers would need to include the "{Resource Provider Namespace}/register/action" operation in their response. This API is used to register for their service, and should include details about the operation (e.g. a localized name for the resource provider + any special considerations like PII release). |
| <CopyableCode code="display" /> | `object` | Contains the localized display information for this particular operation / action. These value will be used by several clients for (1) custom role definitions for RBAC; (2) complex query filters for the event service; and (3) audit history / records for management operations. |
| <CopyableCode code="origin" /> | `string` | Origin. The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. Default value is "user,system". |
| <CopyableCode code="properties" /> | `object` | ClientDiscovery properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Operation to return the list of available operations. |

## `SELECT` examples

Operation to return the list of available operations.


```sql
SELECT
name,
display,
origin,
properties
FROM azure.recovery_services_site_recovery.operations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```