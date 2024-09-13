---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - deploymentmanager
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

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.deploymentmanager.resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | Output only. The name of the resource as it appears in the YAML config. |
| <CopyableCode code="accessControl" /> | `object` | The access controls set on the resource. |
| <CopyableCode code="finalProperties" /> | `string` | Output only. The evaluated properties of the resource with references expanded. Returned as serialized YAML. |
| <CopyableCode code="insertTime" /> | `string` | Output only. Creation timestamp in RFC3339 text format. |
| <CopyableCode code="manifest" /> | `string` | Output only. URL of the manifest representing the current configuration of this resource. |
| <CopyableCode code="properties" /> | `string` | Output only. The current properties of the resource before any references have been filled in. Returned as serialized YAML. |
| <CopyableCode code="type" /> | `string` | Output only. The type of the resource, for example `compute.v1.instance`, or `cloudfunctions.v1beta1.function`. |
| <CopyableCode code="update" /> | `object` |  |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update timestamp in RFC3339 text format. |
| <CopyableCode code="url" /> | `string` | Output only. The URL of the actual resource. |
| <CopyableCode code="warnings" /> | `array` | Output only. If warning messages are generated during processing of this resource, this field will be populated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment, project, resource" /> | Gets information about a single resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment, project" /> | Lists all resources in a given deployment. |

## `SELECT` examples

Lists all resources in a given deployment.

```sql
SELECT
id,
name,
accessControl,
finalProperties,
insertTime,
manifest,
properties,
type,
update,
updateTime,
url,
warnings
FROM google.deploymentmanager.resources
WHERE deployment = '{{ deployment }}'
AND project = '{{ project }}'; 
```
