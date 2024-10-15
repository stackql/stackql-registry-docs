---
title: firewall_policy_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_deployments
  - network
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_deployments" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="deploy" /> | `EXEC` | <CopyableCode code="firewallPolicyName, resourceGroupName, subscriptionId" /> | Deploys the firewall policy draft and child rule collection group drafts. |
