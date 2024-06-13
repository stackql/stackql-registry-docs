---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - cloudhsm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Contains information about an AWS CloudHSM cluster.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains information about an AWS CloudHSM cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudhsm.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="backup_policy" /></td><td><code>string</code></td><td>The cluster's backup policy.</td></tr>
<tr><td><CopyableCode code="backup_retention_policy" /></td><td><code>object</code></td><td>A policy that defines how the service retains backups.</td></tr>
<tr><td><CopyableCode code="cluster_id" /></td><td><code>string</code></td><td>The cluster's identifier (ID).</td></tr>
<tr><td><CopyableCode code="create_timestamp" /></td><td><code>string</code></td><td>The date and time when the cluster was created.</td></tr>
<tr><td><CopyableCode code="hsms" /></td><td><code>array</code></td><td>Contains information about the HSMs in the cluster.</td></tr>
<tr><td><CopyableCode code="hsm_type" /></td><td><code>string</code></td><td>The type of HSM that the cluster contains.</td></tr>
<tr><td><CopyableCode code="pre_co_password" /></td><td><code>string</code></td><td>The default password for the cluster's Pre-Crypto Officer (PRECO) user.</td></tr>
<tr><td><CopyableCode code="security_group" /></td><td><code>string</code></td><td>The identifier (ID) of the cluster's security group.</td></tr>
<tr><td><CopyableCode code="source_backup_id" /></td><td><code>string</code></td><td>The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The cluster's state.</td></tr>
<tr><td><CopyableCode code="state_message" /></td><td><code>string</code></td><td>A description of the cluster's state.</td></tr>
<tr><td><CopyableCode code="subnet_mapping" /></td><td><code>object</code></td><td>A map from availability zone to the cluster’s subnet in that availability zone.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.</td></tr>
<tr><td><CopyableCode code="certificates" /></td><td><code>object</code></td><td>Contains one or more certificates or a certificate signing request (CSR).</td></tr>
<tr><td><CopyableCode code="tag_list" /></td><td><code>array</code></td><td>The list of tags for the cluster.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="describe_clusters" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="create_cluster" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="X-Amz-Target, data__HsmType, data__SubnetIds, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_cluster" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="X-Amz-Target, data__ClusterId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="initialize_cluster" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="X-Amz-Target, data__ClusterId, data__SignedCert, data__TrustAnchor, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="modify_cluster" /></td>
    <td><code>EXEC</code></td>
    <td><CopyableCode code="X-Amz-Target, data__BackupRetentionPolicy, data__ClusterId, region" /></td>
  </tr>
</tbody></table>








