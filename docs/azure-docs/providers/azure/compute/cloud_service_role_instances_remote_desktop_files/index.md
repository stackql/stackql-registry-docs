---
title: cloud_service_role_instances_remote_desktop_files
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_role_instances_remote_desktop_files
  - compute
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

Creates, updates, deletes, gets or lists a <code>cloud_service_role_instances_remote_desktop_files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_service_role_instances_remote_desktop_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_service_role_instances_remote_desktop_files" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | Gets a remote desktop file for a role instance in a cloud service. |

## `SELECT` examples

Gets a remote desktop file for a role instance in a cloud service.


```sql
SELECT

FROM azure.compute.cloud_service_role_instances_remote_desktop_files
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleInstanceName = '{{ roleInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```