---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - monitoring
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

Creates, updates, deletes, gets or lists a <code>members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.monitoring.members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="labels" /> | `object` | Required. Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels "project_id", "instance_id", and "zone". |
| <CopyableCode code="type" /> | `string` | Required. The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_groups_members_list" /> | `SELECT` | <CopyableCode code="groupsId, projectsId" /> | Lists the monitored resources that are members of a group. |

## `SELECT` examples

Lists the monitored resources that are members of a group.

```sql
SELECT
labels,
type
FROM google.monitoring.members
WHERE groupsId = '{{ groupsId }}'
AND projectsId = '{{ projectsId }}'; 
```
