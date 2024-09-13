
---
title: manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - manifests
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

Creates, updates, deletes or gets an <code>manifest</code> resource or lists <code>manifests</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.deploymentmanager.manifests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | Output only. The name of the manifest. |
| <CopyableCode code="config" /> | `object` |  |
| <CopyableCode code="expandedConfig" /> | `string` | Output only. The fully-expanded configuration file, including any templates and references. |
| <CopyableCode code="imports" /> | `array` | Output only. The imported files for this manifest. |
| <CopyableCode code="insertTime" /> | `string` | Output only. Creation timestamp in RFC3339 text format. |
| <CopyableCode code="layout" /> | `string` | Output only. The YAML layout for this manifest. |
| <CopyableCode code="manifestSizeBytes" /> | `string` | Output only. The computed size of the fully expanded manifest. |
| <CopyableCode code="manifestSizeLimitBytes" /> | `string` | Output only. The size limit for expanded manifests in the project. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Self link for the manifest. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deployment, manifest, project" /> | Gets information about a specific manifest. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment, project" /> | Lists all manifests for a given deployment. |

## `SELECT` examples

Lists all manifests for a given deployment.

```sql
SELECT
id,
name,
config,
expandedConfig,
imports,
insertTime,
layout,
manifestSizeBytes,
manifestSizeLimitBytes,
selfLink
FROM google.deploymentmanager.manifests
WHERE deployment = '{{ deployment }}'
AND project = '{{ project }}'; 
```
