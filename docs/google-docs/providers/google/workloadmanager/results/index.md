---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
  - workloadmanager
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
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workloadmanager.results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="documentationUrl" /> | `string` | the document url of the rule |
| <CopyableCode code="resource" /> | `object` | Message represent resource in execution result |
| <CopyableCode code="rule" /> | `string` | the rule which violate in execution |
| <CopyableCode code="severity" /> | `string` | severity of violation |
| <CopyableCode code="violationDetails" /> | `object` | Message describing the violdation in execution result |
| <CopyableCode code="violationMessage" /> | `string` | the violation message of an execution |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="evaluationsId, executionsId, locationsId, projectsId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="evaluationsId, executionsId, locationsId, projectsId" /> |
