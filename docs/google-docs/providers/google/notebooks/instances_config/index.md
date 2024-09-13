---
title: instances_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_config
  - notebooks
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

Creates, updates, deletes, gets or lists a <code>instances_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.notebooks.instances_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availableImages" /> | `array` | Output only. The list of available images to create a WbI. |
| <CopyableCode code="defaultValues" /> | `object` | DefaultValues represents the default configuration values. |
| <CopyableCode code="supportedValues" /> | `object` | SupportedValues represents the values supported by the configuration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets general backend configurations that might also affect the frontend. Location is required by CCFE. Although we could bypass it to send location- less request directly to the backend job, we would need CPE (go/cloud-cpe). Having the location might also be useful depending on the query. |

## `SELECT` examples

Gets general backend configurations that might also affect the frontend. Location is required by CCFE. Although we could bypass it to send location- less request directly to the backend job, we would need CPE (go/cloud-cpe). Having the location might also be useful depending on the query.

```sql
SELECT
availableImages,
defaultValues,
supportedValues
FROM google.notebooks.instances_config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
