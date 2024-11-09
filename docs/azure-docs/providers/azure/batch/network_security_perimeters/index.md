---
title: network_security_perimeters
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeters
  - batch
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_security_perimeters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.network_security_perimeters" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="reconcile_configuration" /> | `EXEC` | <CopyableCode code="accountName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> | Reconciles the specified NSP configuration. |