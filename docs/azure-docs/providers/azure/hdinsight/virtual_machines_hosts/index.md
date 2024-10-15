---
title: virtual_machines_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines_hosts
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>virtual_machines_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machines_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.virtual_machines_hosts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The host name |
| <CopyableCode code="effectiveDiskEncryptionKeyUrl" /> | `string` | The effective disk encryption key URL used by the host |
| <CopyableCode code="fqdn" /> | `string` | The Fully Qualified Domain Name of host |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists the HDInsight clusters hosts |

## `SELECT` examples

Lists the HDInsight clusters hosts


```sql
SELECT
name,
effectiveDiskEncryptionKeyUrl,
fqdn
FROM azure.hdinsight.virtual_machines_hosts
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```