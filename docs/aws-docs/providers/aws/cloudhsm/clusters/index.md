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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudhsm.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `BackupPolicy` | `string` | The cluster's backup policy. |
| `BackupRetentionPolicy` | `object` | A policy that defines the number of days to retain backups. |
| `Certificates` | `object` | Contains one or more certificates or a certificate signing request (CSR). |
| `ClusterId` | `string` | The cluster's identifier (ID). |
| `CreateTimestamp` | `string` | The date and time when the cluster was created. |
| `HsmType` | `string` | The type of HSM that the cluster contains. |
| `Hsms` | `array` | Contains information about the HSMs in the cluster. |
| `PreCoPassword` | `string` | The default password for the cluster's Pre-Crypto Officer (PRECO) user. |
| `SecurityGroup` | `string` | The identifier (ID) of the cluster's security group. |
| `SourceBackupId` | `string` | The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup. |
| `State` | `string` | The cluster's state. |
| `StateMessage` | `string` | A description of the cluster's state. |
| `SubnetMapping` | `object` | A map from availability zone to the cluster’s subnet in that availability zone. |
| `TagList` | `array` | The list of tags for the cluster. |
| `VpcId` | `string` | The identifier (ID) of the virtual private cloud (VPC) that contains the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `describe_clusters` | `SELECT` | `region` | &lt;p&gt;Gets information about AWS CloudHSM clusters.&lt;/p&gt; &lt;p&gt;This is a paginated operation, which means that each response might contain only a subset of all the clusters. When the response contains only a subset of clusters, it includes a &lt;code&gt;NextToken&lt;/code&gt; value. Use this value in a subsequent &lt;code&gt;DescribeClusters&lt;/code&gt; request to get more clusters. When you receive a response with no &lt;code&gt;NextToken&lt;/code&gt; (or an empty or null value), that means there are no more clusters to get.&lt;/p&gt; |
| `create_cluster` | `INSERT` | `X-Amz-Target, data__HsmType, data__SubnetIds, region` | Creates a new AWS CloudHSM cluster. |
| `delete_cluster` | `DELETE` | `X-Amz-Target, data__ClusterId, region` | Deletes the specified AWS CloudHSM cluster. Before you can delete a cluster, you must delete all HSMs in the cluster. To see if the cluster contains any HSMs, use &lt;a&gt;DescribeClusters&lt;/a&gt;. To delete an HSM, use &lt;a&gt;DeleteHsm&lt;/a&gt;. |
| `initialize_cluster` | `EXEC` | `X-Amz-Target, data__ClusterId, data__SignedCert, data__TrustAnchor, region` | Claims an AWS CloudHSM cluster by submitting the cluster certificate issued by your issuing certificate authority (CA) and the CA's root certificate. Before you can claim a cluster, you must sign the cluster's certificate signing request (CSR) with your issuing CA. To get the cluster's CSR, use &lt;a&gt;DescribeClusters&lt;/a&gt;. |
| `modify_cluster` | `EXEC` | `X-Amz-Target, data__BackupRetentionPolicy, data__ClusterId, region` | Modifies AWS CloudHSM cluster. |
