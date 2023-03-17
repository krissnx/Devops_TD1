def train(model, data_loader, epochs=5, batch_size=8): 
    
    optimizer = 'sgd'
    optimizer_params = {'learning_rate': 0.05}
    
    trainer = gluon.Trainer(model.collect_params(), optimizer, optimizer_params)
    loss = gluon.loss.SoftmaxCrossEntropyLoss(sparse_label=False) 

    acc = mx.metric.Accuracy()
    
    for epoch in range(epochs):
        for data, label in data_loader:
            with autograd.record():
                output = model(data)
                output = nd.softmax(output)
                l = loss(output, label)
                acc.update(preds = output, labels=label)
                print(acc.get())
                
            l.backward()
            trainer.step(batch_size)