---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - datafusion
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

Creates, updates, deletes or gets an <code>version</code> resource or lists <code>versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datafusion.versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availableFeatures" /> | `array` | Represents a list of available feature names for a given version. |
| <CopyableCode code="defaultVersion" /> | `boolean` | Whether this is currently the default version for Cloud Data Fusion |
| <CopyableCode code="type" /> | `string` | Type represents the release availability of the version |
| <CopyableCode code="versionNumber" /> | `string` | The version number of the Data Fusion instance, such as '6.0.1.0'. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists possible versions for Data Fusion instances in the specified project and location. |

## `SELECT` examples

Lists possible versions for Data Fusion instances in the specified project and location.

```sql
SELECT
availableFeatures,
defaultVersion,
type,
versionNumber
FROM google.datafusion.versions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
