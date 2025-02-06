class basic_math:

    # create the add function
    def add1(*numbers):
        sumall = 0
        for number in numbers:
            sumall += number
            
        return sumall

    # create the multiply function
    def multiply(*numbers):
        productall = 1
        for number in numbers:
            productall *= number
            
        return productall


class plotting:
    
    def plot_graph(x, y):
        from matplotlib import pyplot as plt
        from matplotlib import style
        
        style.use('ggplot')
        fig, ax = plt.subplots()
        ax.plot(x, y, 'g', label='line1', linewidth=5)
        ax.set_title('CHEE 412-005')
        ax.set_ylabel('$ Revenue')
        ax.set_xlabel('Time (years)')
    
        ax.legend()
        ax.grid(True, color='k')
        plt.savefig('sample_plot.png')
        
        return(ax)
    