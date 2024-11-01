---
title: applied_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - applied_quotas
  - quotas
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applied_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.quotas.applied_quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_environment" /> | `` |  |
| <CopyableCode code="_kafka_cluster" /> | `` |  |
| <CopyableCode code="_network" /> | `` |  |
| <CopyableCode code="_organization" /> | `` |  |
| <CopyableCode code="_user" /> | `` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="applied_limit" /> | `integer` | The latest applied service quota value, taking into account any limit adjustments.<br /> |
| <CopyableCode code="default_limit" /> | `integer` | The default service quota value.<br /> |
| <CopyableCode code="display_name" /> | `string` | A human-readable name for the quota type name. |
| <CopyableCode code="environment" /> | `object` | The environment ID the quota is associated with.<br /> |
| <CopyableCode code="kafka_cluster" /> | `object` | The kafka cluster ID the quota is associated with.<br /> |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="network" /> | `object` | The network ID the quota is associated with.<br /> |
| <CopyableCode code="organization" /> | `object` | A unique organization id to associate a specific organization to this quota. |
| <CopyableCode code="scope" /> | `string` | The applied scope that this quota belongs to. |
| <CopyableCode code="usage" /> | `integer` | Show the quota usage value if the quota usage is available for this quota.<br /> |
| <CopyableCode code="user" /> | `object` | The user associated with this object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_service_quota_v1applied_quota" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Make a request to read an applied quota. |
| <CopyableCode code="list_service_quota_v1applied_quotas" /> | `SELECT` | <CopyableCode code="scope" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Retrieve a sorted, filtered, paginated list of all applied quotas.<br /><br />Shows all quotas for a given scope.<br /> |
