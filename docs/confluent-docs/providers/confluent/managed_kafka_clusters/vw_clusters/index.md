---
title: vw_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - vw_clusters
  - managed_kafka_clusters
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
<tr><td><b>Name</b></td><td><code>vw_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.managed_kafka_clusters.vw_clusters" /></td></tr>
</tbody></table>

## Fields
> This resource is a view. For the view definition, please refer to the provider spec in the [stackql-provider-registry](https://github.com/stackql/stackql-provider-registry/blob/dev/providers/src/confluent/v00.00.00000/services/managed_kafka_clusters.yaml), located under `components -> x-stackQL-resources -> vw_clusters`.

| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `text` |
| <CopyableCode code="api_endpoint" /> | `text` |
| <CopyableCode code="api_version" /> | `text` |
| <CopyableCode code="availability" /> | `text` |
| <CopyableCode code="cloud" /> | `text` |
| <CopyableCode code="config_kind" /> | `text` |
| <CopyableCode code="created_at" /> | `text` |
| <CopyableCode code="display_name" /> | `text` |
| <CopyableCode code="environment" /> ||
| <CopyableCode code="environment_id" /> | `text` |
| <CopyableCode code="environment_related" /> | `text` |
| <CopyableCode code="environment_resource_name" /> | `text` |
| <CopyableCode code="http_endpoint" /> | `text` |
| <CopyableCode code="kafka_bootstrap_endpoint" /> | `text` |
| <CopyableCode code="kind" /> | `text` |
| <CopyableCode code="region" /> | `text` |
| <CopyableCode code="resource_name" /> | `text` |
| <CopyableCode code="self" /> | `text` |
| <CopyableCode code="status_phase" /> | `text` |
| <CopyableCode code="updated_at" /> | `text` |
## Methods
No additional methods available for this resource
