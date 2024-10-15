---
title: pipeline_template_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_template_definitions
  - devops
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

Creates, updates, deletes, gets or lists a <code>pipeline_template_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_template_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devops.pipeline_template_definitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier of the pipeline template. |
| <CopyableCode code="description" /> | `string` | Description of the pipeline enabled by the template. |
| <CopyableCode code="inputs" /> | `array` | List of input parameters required by the template to create a pipeline. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all pipeline templates which can be used to configure an Azure Pipeline. |

## `SELECT` examples

Lists all pipeline templates which can be used to configure an Azure Pipeline.


```sql
SELECT
id,
description,
inputs
FROM azure.devops.pipeline_template_definitions
;
```