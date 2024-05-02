---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Arn` | `string` |  |
| `Certificate` | `string` |  |
| `Domain` | `string` |  |
| `EndpointDetails` | `object` | &lt;p&gt;The virtual private cloud (VPC) endpoint settings that are configured for your file transfer protocol-enabled server. With a VPC endpoint, you can restrict access to your server and resources only within your VPC. To control incoming internet traffic, invoke the &lt;code&gt;UpdateServer&lt;/code&gt; API and attach an Elastic IP address to your server's endpoint.&lt;/p&gt; &lt;note&gt; &lt;p&gt; After May 19, 2021, you won't be able to create a server using &lt;code&gt;EndpointType=VPC_ENDPOINT&lt;/code&gt; in your Amazon Web Servicesaccount if your account hasn't already done so before May 19, 2021. If you have already created servers with &lt;code&gt;EndpointType=VPC_ENDPOINT&lt;/code&gt; in your Amazon Web Servicesaccount on or before May 19, 2021, you will not be affected. After this date, use &lt;code&gt;EndpointType&lt;/code&gt;=&lt;code&gt;VPC&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.&lt;/p&gt; &lt;/note&gt; |
| `EndpointType` | `string` |  |
| `HostKeyFingerprint` | `string` |  |
| `IdentityProviderDetails` | `object` | Returns information related to the type of user authentication that is in use for a file transfer protocol-enabled server's users. A server can have only one method of authentication. |
| `IdentityProviderType` | `string` | &lt;p&gt;The mode of authentication for a server. The default value is &lt;code&gt;SERVICE_MANAGED&lt;/code&gt;, which allows you to store and access user credentials within the Transfer Family service.&lt;/p&gt; &lt;p&gt;Use &lt;code&gt;AWS_DIRECTORY_SERVICE&lt;/code&gt; to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the &lt;code&gt;IdentityProviderDetails&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;API_GATEWAY&lt;/code&gt; value to integrate with an identity provider of your choosing. The &lt;code&gt;API_GATEWAY&lt;/code&gt; setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the &lt;code&gt;IdentityProviderDetails&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;Use the &lt;code&gt;AWS_LAMBDA&lt;/code&gt; value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the &lt;code&gt;Function&lt;/code&gt; parameter for the &lt;code&gt;IdentityProviderDetails&lt;/code&gt; data type.&lt;/p&gt; |
| `LoggingRole` | `string` |  |
| `PostAuthenticationLoginBanner` | `string` |  |
| `PreAuthenticationLoginBanner` | `string` |  |
| `ProtocolDetails` | `object` |  The protocol settings that are configured for your server.  |
| `Protocols` | `array` |  |
| `SecurityPolicyName` | `string` |  |
| `ServerId` | `string` |  |
| `State` | `string` | &lt;p&gt;Describes the condition of a file transfer protocol-enabled server with respect to its ability to perform file operations. There are six possible states: &lt;code&gt;OFFLINE&lt;/code&gt;, &lt;code&gt;ONLINE&lt;/code&gt;, &lt;code&gt;STARTING&lt;/code&gt;, &lt;code&gt;STOPPING&lt;/code&gt;, &lt;code&gt;START_FAILED&lt;/code&gt;, and &lt;code&gt;STOP_FAILED&lt;/code&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;OFFLINE&lt;/code&gt; indicates that the server exists, but that it is not available for file operations. &lt;code&gt;ONLINE&lt;/code&gt; indicates that the server is available to perform file operations. &lt;code&gt;STARTING&lt;/code&gt; indicates that the server's was instantiated, but the server is not yet available to perform file operations. Under normal conditions, it can take a couple of minutes for the server to be completely operational. Both &lt;code&gt;START_FAILED&lt;/code&gt; and &lt;code&gt;STOP_FAILED&lt;/code&gt; are error conditions.&lt;/p&gt; |
| `StructuredLogDestinations` | `array` |  |
| `Tags` | `array` |  |
| `UserCount` | `integer` |  |
| `WorkflowDetails` | `object` | Container for the &lt;code&gt;WorkflowDetail&lt;/code&gt; data type. It is used by actions that trigger a workflow to begin execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `describe_server` | `SELECT` | `data__ServerId, region` | &lt;p&gt;Describes a file transfer protocol-enabled server that you specify by passing the &lt;code&gt;ServerId&lt;/code&gt; parameter.&lt;/p&gt; &lt;p&gt;The response contains a description of a server's properties. When you set &lt;code&gt;EndpointType&lt;/code&gt; to VPC, the response will contain the &lt;code&gt;EndpointDetails&lt;/code&gt;.&lt;/p&gt; |
| `list_servers` | `SELECT` | `region` | Lists the file transfer protocol-enabled <br />servers that are associated with your <br />Amazon Web Services account.<br /> |
| `create_server` | `INSERT` | `region` | Instantiates an auto-scaling virtual server based on the selected file transfer protocol in Amazon Web Services. When you make updates to your file transfer protocol-enabled server or when you work with users, use the service-generated &lt;code&gt;ServerId&lt;/code&gt; property that is assigned to the newly created server. |
| `delete_server` | `DELETE` | `data__ServerId, region` | &lt;p&gt;Deletes the file transfer protocol-enabled server that you specify.&lt;/p&gt; &lt;p&gt;No response returns from this operation.&lt;/p&gt; |
| `update_server` | `UPDATE` | `data__ServerId, region` | &lt;p&gt;Updates the file transfer protocol-enabled server's properties after that server has been created.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;UpdateServer&lt;/code&gt; call returns the &lt;code&gt;ServerId&lt;/code&gt; of the server you updated.&lt;/p&gt; |
