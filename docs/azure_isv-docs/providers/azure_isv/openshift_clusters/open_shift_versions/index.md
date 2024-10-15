---
title: open_shift_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - open_shift_versions
  - openshift_clusters
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

Creates, updates, deletes, gets or lists a <code>open_shift_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_shift_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.openshift_clusters.open_shift_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | OpenShiftVersionProperties represents the properties of an OpenShiftVersion. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | The operation returns the installable OpenShift versions as strings. |

## `SELECT` examples

The operation returns the installable OpenShift versions as strings.


```sql
SELECT
properties,
systemData
FROM azure_isv.openshift_clusters.open_shift_versions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```