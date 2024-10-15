---
title: published_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - published_artifacts
  - blueprints
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

Creates, updates, deletes, gets or lists a <code>published_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>published_artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.published_artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="kind" /> | `string` | Specifies the kind of blueprint artifact. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactName, blueprintName, resourceScope, versionId" /> | Get an artifact for a published blueprint definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope, versionId" /> | List artifacts for a version of a published blueprint definition. |

## `SELECT` examples

List artifacts for a version of a published blueprint definition.


```sql
SELECT
id,
name,
kind,
type
FROM azure.blueprints.published_artifacts
WHERE blueprintName = '{{ blueprintName }}'
AND resourceScope = '{{ resourceScope }}'
AND versionId = '{{ versionId }}';
```