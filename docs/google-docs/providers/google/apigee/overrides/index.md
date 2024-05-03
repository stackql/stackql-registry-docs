---
title: overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - overrides
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>overrides</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.overrides" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | ID of the trace configuration override specified as a system-generated UUID. |
| <CopyableCode code="apiProxy" /> | `string` | ID of the API proxy that will have its trace configuration overridden. |
| <CopyableCode code="samplingConfig" /> | `object` | TraceSamplingConfig represents the detail settings of distributed tracing. Only the fields that are defined in the distributed trace configuration can be overridden using the distribute trace configuration override APIs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_trace_config_overrides_get" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId, overridesId" /> | Gets a trace configuration override. |
| <CopyableCode code="organizations_environments_trace_config_overrides_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Lists all of the distributed trace configuration overrides in an environment. |
| <CopyableCode code="organizations_environments_trace_config_overrides_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Creates a trace configuration override. The response contains a system-generated UUID, that can be used to view, update, or delete the configuration override. Use the List API to view the existing trace configuration overrides. |
| <CopyableCode code="organizations_environments_trace_config_overrides_delete" /> | `DELETE` | <CopyableCode code="environmentsId, organizationsId, overridesId" /> | Deletes a distributed trace configuration override. |
| <CopyableCode code="_organizations_environments_trace_config_overrides_list" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId" /> | Lists all of the distributed trace configuration overrides in an environment. |
| <CopyableCode code="organizations_environments_trace_config_overrides_patch" /> | `EXEC` | <CopyableCode code="environmentsId, organizationsId, overridesId" /> | Updates a distributed trace configuration override. Note that the repeated fields have replace semantics when included in the field mask and that they will be overwritten by the value of the fields in the request body. |
