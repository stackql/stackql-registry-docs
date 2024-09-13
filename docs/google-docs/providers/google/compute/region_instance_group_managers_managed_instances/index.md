
---
title: region_instance_group_managers_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instance_group_managers_managed_instances
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

Creates, updates, deletes or gets an <code>region_instance_group_managers_managed_instance</code> resource or lists <code>region_instance_group_managers_managed_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instance_group_managers_managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instance_group_managers_managed_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedInstances" /> | `array` | A list of managed instances. |
| <CopyableCode code="nextPageToken" /> | `string` | [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger than maxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_managed_instances" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, region" /> | Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`. |

## `SELECT` examples

Lists the instances in the managed instance group and instances that are scheduled to be created. The list includes any current actions that the group has scheduled for its instances. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

```sql
SELECT
managedInstances,
nextPageToken
FROM google.compute.region_instance_group_managers_managed_instances
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND region = '{{ region }}'; 
```
