
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>result</code> resource or lists <code>results</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workloadmanager.results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="commands" /> | `array` | The commands to remediate the violation. |
| <CopyableCode code="documentationUrl" /> | `string` | The URL for the documentation of the rule. |
| <CopyableCode code="resource" /> | `object` | Message represent resource in execution result |
| <CopyableCode code="rule" /> | `string` | The rule that is violated in an evaluation. |
| <CopyableCode code="severity" /> | `string` | The severity of violation. |
| <CopyableCode code="violationDetails" /> | `object` | Message describing the violation in an evaluation result. |
| <CopyableCode code="violationMessage" /> | `string` | The violation message of an execution. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="evaluationsId, executionsId, locationsId, projectsId" /> | Lists the result of a single evaluation. |

## `SELECT` examples

Lists the result of a single evaluation.

```sql
SELECT
commands,
documentationUrl,
resource,
rule,
severity,
violationDetails,
violationMessage
FROM google.workloadmanager.results
WHERE evaluationsId = '{{ evaluationsId }}'
AND executionsId = '{{ executionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
