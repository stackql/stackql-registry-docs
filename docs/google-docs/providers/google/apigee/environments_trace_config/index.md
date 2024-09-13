---
title: environments_trace_config
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_trace_config
  - apigee
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

Creates, updates, deletes or gets an <code>environments_trace_config</code> resource or lists <code>environments_trace_config</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_trace_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.environments_trace_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpoint" /> | `string` | Required. Endpoint of the exporter. |
| <CopyableCode code="exporter" /> | `string` | Required. Exporter that is used to view the distributed trace captured using OpenCensus. An exporter sends traces to any backend that is capable of consuming them. Recorded spans can be exported by registered exporters. |
| <CopyableCode code="samplingConfig" /> | `object` | TraceSamplingConfig represents the detail settings of distributed tracing. Only the fields that are defined in the distributed trace configuration can be overridden using the distribute trace configuration override APIs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_get_trace_config" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Get distributed trace configuration in an environment. |
| <CopyableCode code="organizations_environments_update_trace_config" /> | `UPDATE` | <CopyableCode code="environmentsId, organizationsId" /> | Updates the trace configurations in an environment. Note that the repeated fields have replace semantics when included in the field mask and that they will be overwritten by the value of the fields in the request body. |

## `SELECT` examples

Get distributed trace configuration in an environment.

```sql
SELECT
endpoint,
exporter,
samplingConfig
FROM google.apigee.environments_trace_config
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `UPDATE` example

Updates a environments_trace_config only if the necessary resources are available.

```sql
UPDATE google.apigee.environments_trace_config
SET 
exporter = '{{ exporter }}',
samplingConfig = '{{ samplingConfig }}',
endpoint = '{{ endpoint }}'
WHERE 
environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}';
```
