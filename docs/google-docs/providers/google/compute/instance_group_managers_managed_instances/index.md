
---
title: instance_group_managers_managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_group_managers_managed_instances
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

Creates, updates, deletes or gets an <code>instance_group_managers_managed_instance</code> resource or lists <code>instance_group_managers_managed_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_group_managers_managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instance_group_managers_managed_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedInstances" /> | `array` | [Output Only] The list of instances in the managed instance group. |
| <CopyableCode code="nextPageToken" /> | `string` | [Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger than maxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_managed_instances" /> | `SELECT` | <CopyableCode code="instanceGroupManager, project, zone" /> | Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`. |

## `SELECT` examples

Lists all of the instances in the managed instance group. Each instance in the list has a currentAction, which indicates the action that the managed instance group is performing on the instance. For example, if the group is still creating an instance, the currentAction is CREATING. If a previous action failed, the list displays the errors for that failed action. The orderBy query parameter is not supported. The `pageToken` query parameter is supported only if the group's `listManagedInstancesResults` field is set to `PAGINATED`.

```sql
SELECT
managedInstances,
nextPageToken
FROM google.compute.instance_group_managers_managed_instances
WHERE instanceGroupManager = '{{ instanceGroupManager }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```
