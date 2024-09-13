---
title: test_environment_catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - test_environment_catalog
  - testing
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

Creates, updates, deletes, gets or lists a <code>test_environment_catalog</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_environment_catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.testing.test_environment_catalog" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="androidDeviceCatalog" /> | `object` | The currently supported Android devices. |
| <CopyableCode code="deviceIpBlockCatalog" /> | `object` | List of IP blocks used by the Firebase Test Lab |
| <CopyableCode code="iosDeviceCatalog" /> | `object` | The currently supported iOS devices. |
| <CopyableCode code="networkConfigurationCatalog" /> | `object` |  |
| <CopyableCode code="softwareCatalog" /> | `object` | The currently provided software environment on the devices under test. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentType" /> | Gets the catalog of supported test environments. May return any of the following canonical error codes: - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the environment type does not exist - INTERNAL - if an internal error occurred |

## `SELECT` examples

Gets the catalog of supported test environments. May return any of the following canonical error codes: - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the environment type does not exist - INTERNAL - if an internal error occurred

```sql
SELECT
androidDeviceCatalog,
deviceIpBlockCatalog,
iosDeviceCatalog,
networkConfigurationCatalog,
softwareCatalog
FROM google.testing.test_environment_catalog
WHERE environmentType = '{{ environmentType }}'; 
```
