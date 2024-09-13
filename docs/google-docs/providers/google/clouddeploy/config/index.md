---
title: config
hide_title: false
hide_table_of_contents: false
keywords:
  - config
  - clouddeploy
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

Creates, updates, deletes, gets or lists a <code>config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the configuration. |
| <CopyableCode code="defaultSkaffoldVersion" /> | `string` | Default Skaffold version that is assigned when a Release is created without specifying a Skaffold version. |
| <CopyableCode code="supportedVersions" /> | `array` | All supported versions of Skaffold. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_config" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets the configuration for a location. |

## `SELECT` examples

Gets the configuration for a location.

```sql
SELECT
name,
defaultSkaffoldVersion,
supportedVersions
FROM google.clouddeploy.config
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
