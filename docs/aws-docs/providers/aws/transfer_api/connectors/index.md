---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - transfer_api
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
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `AccessRole` | `string` |  |
| `Arn` | `string` |  |
| `As2Config` | `object` | Contains the details for an AS2 connector object. The connector object is used for AS2 outbound processes, to connect the Transfer Family customer with the trading partner. |
| `ConnectorId` | `string` |  |
| `LoggingRole` | `string` |  |
| `SftpConfig` | `object` | Contains the details for an SFTP connector object. The connector object is used for transferring files to and from a partner's SFTP server. |
| `Tags` | `array` |  |
| `Url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `describe_connector` | `SELECT` | `data__ConnectorId, region` | Describes the connector that's identified by the &lt;code&gt;ConnectorId.&lt;/code&gt;  |
| `list_connectors` | `SELECT` | `region` | Lists the connectors for the specified Region. |
| `create_connector` | `INSERT` | `data__AccessRole, data__Url, region` | &lt;p&gt;Creates the connector, which captures the parameters for an outbound connection for the AS2 or SFTP protocol. The connector is required for sending files to an externally hosted AS2 or SFTP server. For more details about AS2 connectors, see &lt;a href="https://docs.aws.amazon.com/transfer/latest/userguide/create-b2b-server.html#configure-as2-connector"&gt;Create AS2 connectors&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;You must specify exactly one configuration object: either for AS2 (&lt;code&gt;As2Config&lt;/code&gt;) or SFTP (&lt;code&gt;SftpConfig&lt;/code&gt;).&lt;/p&gt; &lt;/note&gt; |
| `delete_connector` | `DELETE` | `data__ConnectorId, region` | Deletes the connector that's specified in the provided &lt;code&gt;ConnectorId&lt;/code&gt;. |
| `update_connector` | `UPDATE` | `data__ConnectorId, region` | Updates some of the parameters for an existing connector. Provide the &lt;code&gt;ConnectorId&lt;/code&gt; for the connector that you want to update, along with the new values for the parameters to update. |
